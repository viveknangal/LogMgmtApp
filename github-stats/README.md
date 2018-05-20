# Github Stats Application
This is a Dockerized Application which publishes meta-data details(like Clone URL,Last Commit date) about GitHub Public Repositories based on the file input.

Its written in Python language which internally make use of GitHub REST API's to fetch the Repo details.
## Prerequisite to run this Application
* **Docker** should to be installed
* **Input FileName** should be provided as an command line argument which has list of repositories i.e One repo per input line, format: $orgname/$repo, e.g. kubernetes/charts.
* **Mount** the current directory onto Docker which has the *Input FileName*

Refer below snippet on how to pass command line argument & mount directory.

 ## How to Build Docker Image
Run the **docker build** from the same directory which has the Dockerfile
```
docker build --no-cache -t honestbee:latest .
```

## How to use this Docker Image

```sh
$ docker run -e input_file_name=input.txt -e output_file_name=output.csv -v "$(pwd)":/app honestbee:latest
```
#### Docker **Run** command make use of below command line options:
* Environment variable(-e)
  * **input_file_name** = Application will read this **input_file_name** to fetch the meta-data about the listed repositories.
  * **output_file_name** = This is a CSV format file to which Application will write the contents in One line per input repo/
* Volume Mount(-v)
  * This option is being used to mount the current directory in Docker instance. Above mentioned **input_file_name** should       exists in this location & here only the **output_file_name** will be created.
 

## Sample Input
 The **input_file_name** should include data in below format:
```
viveknangal/flask
kubernetes/charts
kubernetes/examples
```
 
 ## Sample Output
 Docker **RUN** command produces two kind of outputs:
 * Tabular Format : This form of output is displayed on STDOUT.
 * CSV Format : This form of output produces a CSV formatted file ,which get published on mounted file system.
    
 > docker run -e input_file_name=input.txt -e output_file_name=output.csv -v "$(pwd)":/app honestbee:latest
 ```
INFO:root:......Program Started......
+-----------+--------------------------------------------+-----------------------+-----------------+
| Repo_Name |                 Clone URL                  | Date of Latest Commit |      Author     |
+-----------+--------------------------------------------+-----------------------+-----------------+
|   flask   |  https://github.com/viveknangal/flask.git  |  2018-05-15T11:40:25Z |      vivek      |
|   charts  |  https://github.com/kubernetes/charts.git  |  2018-05-18T22:17:51Z | Lachlan Evenson |
|  examples | https://github.com/kubernetes/examples.git |  2018-05-02T08:53:57Z |     foo0x29a    |
+-----------+--------------------------------------------+-----------------------+-----------------+
CSV format output file= output.csv
 
 
 ```
