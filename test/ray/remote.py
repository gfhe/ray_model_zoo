import ray

ray.init(address='localhost:8256')


@ray.remote(num_cpus=2, max_calls=3, max_restarts=1)
def add(a, b):
    return a + b


for i in range(10):
    result = ray.get(add.remote(1, i))
    print(result)
