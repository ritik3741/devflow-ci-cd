import os
import click
import yaml
from pathlib import Path

# -------------------------------------------------
# Load configuration from devflow.yaml
# -------------------------------------------------
def load_config():
    config_path = Path("devflow.yaml")

    if not config_path.exists():
        raise FileNotFoundError(
            "❌ devflow.yaml not found. Run the CLI from the project root."
        )

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    if not config:
        raise ValueError("❌ devflow.yaml is empty or invalid")

    return config


# -------------------------------------------------
# Root CLI group
# -------------------------------------------------
@click.group()
def cli():
    """DevFlow CLI – Internal DevOps Automation Tool"""
    pass


# -------------------------------------------------
# Deploy command (with --env and --dry-run)
# -------------------------------------------------
@cli.command()
@click.option(
    "--env",
    default="dev",
    type=click.Choice(["dev", "prod"]),
    help="Deployment environment (dev or prod)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show actions without executing them",
)
def deploy(env, dry_run):
    """Deploy DevFlow to Kubernetes"""
    config = load_config()

    app_name = config["app"]["name"]
    dockerfile = config["docker"]["dockerfile"]
    env_config = config["environments"][env]

    image = env_config["image"]
    deployment_path = env_config["deployment_path"]
    deployment_name = config["kubernetes"]["deployment_name"]

    click.echo(f"🚀 Deploying {app_name.upper()} to {env.upper()} environment")

    def run(cmd):
        if dry_run:
            click.echo(f"[DRY-RUN] {cmd}")
        else:
            os.system(cmd)

    # Build image only for DEV
    if env == "dev":
        click.echo("🔧 Docker build (DEV)")
        run(f"docker build -t {image} -f {dockerfile} .")

    click.echo("📦 Applying Kubernetes manifests")
    run(f"kubectl apply -f {deployment_path}/deployment.yaml")
    run(f"kubectl apply -f {deployment_path}/service.yaml")

    click.echo("🔄 Restarting deployment")
    run(f"kubectl rollout restart deployment {deployment_name}")

    click.echo("✅ Deployment finished")


# -------------------------------------------------
# Rollback command
# -------------------------------------------------
@cli.command()
def rollback():
    """Rollback Kubernetes deployment to previous revision"""
    click.echo("⏪ Rolling back deployment to previous revision")
    os.system("kubectl rollout undo deployment devflow-deployment")
    click.echo("✅ Rollback complete")


# -------------------------------------------------
# Status command
# -------------------------------------------------
@cli.command()
def status():
    """Show Kubernetes pod status"""
    os.system("kubectl get pods")


# -------------------------------------------------
# Logs command
# -------------------------------------------------
@cli.command()
def logs():
    """View application logs"""
    os.system("kubectl logs deployment/devflow-deployment")


# -------------------------------------------------
# Cleanup command
# -------------------------------------------------
@cli.command()
def cleanup():
    """Delete Kubernetes deployment and service"""
    os.system("kubectl delete service devflow-service")
    os.system("kubectl delete deployment devflow-deployment")
    click.echo("✅ Cleanup complete")


# -------------------------------------------------
# Entry point for console_scripts
# -------------------------------------------------
def main():
    cli()


if __name__ == "__main__":
    main()
