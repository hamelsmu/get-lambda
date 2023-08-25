import argparse
from lambdacloud import create_instance
from lambdacloud import login
import os
import time

def main(instance_type):
    sleep_time = 10
    login(token=os.getenv('LAMBDA_CLOUD_TOKEN'))

    while True:
        try:
            instance_id = create_instance(instance_type, ssh_key_names="lambda-new")
            print(f'Instance created with id: {instance_id}')
            break
        except:
            print(f'No desired instance found...sleeping for {sleep_time} seconds')
            time.sleep(sleep_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance_type", type=str, required=True, help="Instance type to be created.")
    args = parser.parse_args()
    main(args.instance_type)
