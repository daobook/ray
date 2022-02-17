import click
import ray
import time


def num_alive_nodes():
    return sum(bool(node["Alive"]) for node in ray.nodes())


@click.command()
@click.option(
    "--num-nodes", required=True, type=int, help="The target number of nodes")
def wait_cluster(num_nodes: int):
    ray.init(address="auto")
    while num_alive_nodes() != num_nodes:
        print(f"Waiting for nodes: {num_alive_nodes()}/{num_nodes}")
        time.sleep(5)


if __name__ == "__main__":
    wait_cluster()
