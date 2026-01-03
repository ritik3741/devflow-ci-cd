import os
import click
import yaml
from pathlib import Path


# ---------------------------
# Load configuration
# ---------------------------
def load_config():
    config_path = Path("devflow.yaml")

    if not config_path.exists():
        raise FileNotFoundError("❌ devflow.yaml not found. Run CLI from project root.")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    if not config:
        raise ValueError("❌ devflow.yaml is empty or invalid")

    return config


# ---------------------------
# CLI root
# ---------------------------
@click.group()
def cli():
    """DevFlow CLI – Internal DevOps Tool"""
    pass


# ---------------------------
# Deploy command
# ---------------------------
@cli.command()
@click.option(
    "--env",
    default="dev",
    type=click.Choice(["dev", "prod"]),
    help="Deployment environment (dev or prod)"
)
def deploy(env):
    """Deploy DevFlow to Kubernetes using config"""
    config = load_config()

    app_name = config["app"]["name"]
    dockerfile = config["docker"]["dockerfile"]
    env_config = config["environments"][env]

    image = env_config["image"]
    deployment_path = env_config["deployment_path"]

    deployment_name = config["kubernetes"]["deployment_name"]

    click.echo(f"🚀 Deploying {app_name.upper()} to {env.upper()} environment")

    # Build image only for DEV
    if env == "dev":
        click.echo("🔧 Building Docker image (DEV)")
        os.system(f"docker build -t {image} -f {dockerfile} .")

    click.echo("📦 Applying Kubernetes manifests")
    os.system(f"kubectl apply -f {deployment_path}/deployment.yaml")
    os.system(f"kubectl apply -f {deployment_path}/service.yaml")

    click.echo("🔄 Restarting deployment")
    os.system(f"kubectl rollout restart deployment {deployment_name}")

    click.echo("✅ Deployment complete")


# ---------------------------
# Status command
# ---------------------------
@cli.command()
def status():
    """Check Kubernetes pod status"""
    os.system("kubectl get pods")


# ---------------------------
# Logs command
# ---------------------------
@cli.command()
def logs():
    """View application logs"""
    os.system("kubectl logs deployment/devflow-deployment")


# ---------------------------
# Cleanup command
# ---------------------------
@cli.command()
def cleanup():
    """Delete Kubernetes resources"""
    os.system("kubectl delete service devflow-service")
    os.system("kubectl delete deployment devflow-deployment")
    click.echo("✅ Cleanup complete")


# ---------------------------
# Entry point
# ---------------------------
def main():
    cli()


if __name__ == "__main__":
    main()
