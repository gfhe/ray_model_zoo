
## local 部署和测试

下面是一个使用ray.remote的示例，并详细说明如何部署和运行该示例：

1. 首先，确保已经安装了Ray，并且版本是2.4.0。可以使用以下命令来检查Ray的版本：

   ````
   pip show ray
   ```

   如果版本不是2.4.0，请使用以下命令升级Ray：

   ````
   pip install --upgrade ray==2.4.0
   ```

2. 接下来，创建一个Python文件，并将以下代码复制到文件中：

   ````python
   import ray

   ray.init()

   @ray.remote
   def add(a, b):
       return a + b

   result = ray.get(add.remote(1, 2))
   print(result)
   ```

   在这个例子中，我们定义了一个函数`add`，并使用`@ray.remote`装饰器将其转换为一个远程函数。然后，我们通过调用`add.remote(1, 2)`来异步地远程调用该函数，返回一个对象句柄。最后，我们使用`ray.get`来获取异步调用的结果，结果为3。

3. 接下来，将文件保存为`example.py`。

4. 现在，我们需要在本地启动Ray集群。在终端中输入以下命令：

   ````
   ray start --head
   ```

   这将启动一个本地Ray集群，并将控制台输出如下：

   ````
   Local node IP: 127.0.0.1
   2021-12-12 16:35:34,362 INFO services.py:1260 -- View the Ray dashboard at http://127.0.0.1:8265
   ```

   请注意，此命令将在后台运行Ray集群，并保持运行状态，直到您手动停止它。

5. 接下来，我们可以在另一个终端中运行我们的Python文件。在终端中输入以下命令：

   ````
   python example.py
   ```

   这将运行我们的Python文件，并在控制台输出结果`3`。

6. 最后，当我们完成所有操作后，可以使用以下命令来停止本地Ray集群：

   ````
   ray stop
   ```

   这将停止在步骤4中启动的Ray集群。

   请注意，如果您希望在生产环境中使用Ray集群，请参考Ray文档中的指南，以确保安全和可靠的部署。
   


## ray cluster 部署

要将上述示例提交到Ray集群上运行，需要按照以下步骤进行操作：

1. 首先，确保已经安装了Ray，并且版本是2.4.0。可以使用以下命令来检查Ray的版本：

   ````
   pip show ray
   ```

   如果版本不是2.4.0，请使用以下命令升级Ray：

   ````
   pip install --upgrade ray==2.4.0
   ```

2. 然后，需要在Ray集群上启动一个Head节点。此节点将作为集群的控制中心，负责协调任务分配和资源管理。可以使用以下命令在Head节点上启动Ray集群：

   ````
   ray start --head --port=6379 --num-cpus=4 --redis-password=<password>
   ```

   这将启动一个名为`ray-head`的Head节点，使用端口号`6379`和密码`<password>`。请注意，`--num-cpus`选项指定Head节点可用的CPU数量。您可以根据需要调整此值。

3. 接下来，需要在集群上启动一个或多个Worker节点。这些节点将处理任务并执行远程调用。可以使用以下命令在Worker节点上启动Ray集群：

   ````
   ray start --address=<ray_head_address>:6379 --redis-password=<password> --num-cpus=4
   ```

   在这个命令中，`<ray_head_address>`应替换为Head节点的IP地址或主机名。此命令还使用与Head节点相同的端口和密码，并指定Worker节点可用的CPU数量。

   您可以在需要的地方多次运行此命令，以启动多个Worker节点。

4. 在启动集群的过程中，请确保所有节点都已成功启动，并且可以在Head节点上看到它们的信息。可以使用以下命令查看集群状态：

   ````
   ray status
   ```

   这将显示集群的当前状态，以及Head节点和Worker节点的信息。

5. 然后，将上述Python代码复制到一个名为`example.py`的文件中，并使用以下命令将其提交到Ray集群上：

   ````
   ray submit example.py --address=<ray_head_address>:6379 --redis-password=<password>
   ```

   在这个命令中，`<ray_head_address>`应替换为Head节点的IP地址或主机名。此命令还使用与Head节点相同的端口和密码。

   当您运行此命令时，Ray将在集群中自动启动一个新的任务，并将Python文件发送到其中一个Worker节点。然后，Worker节点将执行Python代码，并将结果返回给Head节点。

6. 最后，您可以使用以下命令查看任务的状态和输出：

   ````
   ray status
   ```

   这将显示集群的当前状态，包括任务的状态和输出。如果任务已成功完成，则可以在输出中找到结果。

   请注意，您还可以使用其他Ray命令来管理集群和任务。有关更多信息，请参阅Ray文档。