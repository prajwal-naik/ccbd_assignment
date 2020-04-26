package Locations;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class LocMapper extends MapReduceBase implements Mapper <LongWritable, Text, Text, IntWritable> {
	//private final static IntWritable one = new IntWritable(1);

	public void map(LongWritable key, Text value, OutputCollector <Text, IntWritable> output, Reporter reporter) throws IOException {

		String valueString = value.toString();
		String[] SingleLocData = valueString.split(",");
		output.collect(new Text(SingleLocData[1]), new IntWritable(Integer.parseInt(SingleLocData[2]))); //the output format to be sent to LocReducer.java
	}
}
