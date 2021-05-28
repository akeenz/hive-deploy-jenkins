DIR="artifact_folder/"
if [ -d "$DIR" ]; then
  # Take action if $DIR exists. #
  rm -rf ${DIR}
  echo "I'm deleting  ${DIR}..."
fi
DIR1="emr-hive-dataset/"
if [ -d "$DIR1" ]; then
  # Take action if $DIR exists. #
  rm -rf ${DIR1}
  echo "I'm deleting  ${DIR1}..."
fi
