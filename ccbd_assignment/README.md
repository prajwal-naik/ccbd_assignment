Check if environment varible `$HADOOP_HOME` is set. If not, set it using the command, 
`export HADOOP_HOME=/usr/share/hadoop`
Note : The hadoop installation files need to be present in the directory mentioned in the command.

Grant the necessary read permissions to the files in the MapReduceCcbd.

Set  `$CLASSPATH` using the command, 
`export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.10.0.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-2.10.0.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-2.10.0.jar:~/MapReduceTutorial/SalesCountry/*:$HADOOP_HOME/lib/*"`
Note: make sure to use the hadoop version installed in your system

Compile all .java files and create a manfest file, Manifest.txt. Create a .jar file using the command, 
`jar cfm GreennessAtLocation Manifest.txt Locations/*.class`

Start hadoop and copy the input folder, with the .csv files, to the hdfs using the command, 
`sudo $HADOOP_HOME/bin/hdfs dfs -copyFromLocal ~/inputMapReduce /`

Run the mapreduce job using, 
`sudo $HADOOP_HOME/bin/hadoop jar ProductSalePerCountry.jar /inputMapReduce /outputMapReduce`

Copy the output file from hdfs to your local file system for viewing using, `$HADOOP_HOME/bin/hdfs dfs -copyToLocal /outputMapReduce /MapReduceCcbd`