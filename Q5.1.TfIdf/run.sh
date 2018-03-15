# Create the input directory
hdfs dfs -mkdir -p /q51/input

# Download the files needed for this exercise and put them in the input directory in the HDFS
wget http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt
hdfs dfs -copyFromLocal defoe-robinson-103.txt /q51/input

wget http://www.textfiles.com/etext/FICTION/callwild
hdfs dfs -copyFromLocal callwild /q51/input

# Run round 1
hadoop jar ../hadoop-streaming-3.0.0.jar \
-input /q51/input \
-output /q51/out_round1 \
-file ./mapper1.py \
-mapper mapper1.py \
-file ./reducer1.py \
-reducer reducer1.py

# Run round 2
hadoop jar ../hadoop-streaming-3.0.0.jar \
-input /q51/out_round1 \
-output /q51/out_round2 \
-file ./mapper2.py \
-mapper mapper2.py \
-file ./reducer2.py \
-reducer reducer2.py

# Run round 3
hadoop jar ../hadoop-streaming-3.0.0.jar \
-input /q51/out_round2 \
-output /q51/out_round3 \
-file ./mapper3.py \
-mapper mapper3.py \
-file ./reducer3.py \
-reducer reducer3.py

# Run round 4
hadoop jar ../hadoop-streaming-3.0.0.jar \
-numReduceTasks 0 \
-input /q51/out_round3 \
-output /q51/out_round4 \
-file ./tf_idf.py \
-mapper tf_idf.py \
-file ./final_reducer.py \
-reducer final_reducer.py 

hdfs dfs -get /q51

cat ./q51/out_round4/part-00000 | python top20.py