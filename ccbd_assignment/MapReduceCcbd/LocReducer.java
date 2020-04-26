package Locations;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class LocReducer extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable> {

	public void reduce(Text t_key, Iterator<IntWritable> values, OutputCollector<Text,IntWritable> output, Reporter reporter) throws IOException {
		Text key = t_key;
		//int threshold = 30;
		while (values.hasNext()) {
			IntWritable value = (IntWritable) values.next();
			if(value.get()>50) //the threshold value has been set to 50 because, there seem to be no places in urban Bangalore with more than 75% greenery. 
			{
				output.collect(key, new IntWritable(value.get()));
			}
		}
		/*if(values.next().get() > 30){
			output.collect(key, new IntWritable(values.next().get()));
		}*/
	}
}




