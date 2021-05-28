DIR="artifact_folder/"
if [ -d "$DIR" ]; then
  # Take action if $DIR exists. #
  rm -rf ${DIR}
  echo "I'm deleting  ${DIR}..."
fi
pwd