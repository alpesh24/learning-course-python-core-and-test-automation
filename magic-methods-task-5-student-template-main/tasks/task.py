import os
import shutil
import uuid

class TempDir:
   def __enter__(self):
        # Create a random, unique directory name
        self.temp_dir = str(uuid.uuid4())

        # Save the current working directory    
        self.prev_dir = os.getcwd()

        # Create a temporary directory
        os.mkdir(self.temp_dir)

        # Change the current working directory to the temporary directory
        os.chdir(self.temp_dir)

        return self.temp_dir
   
   def __exit__(self, exc_type, exc_value, traceback):
      # Change the working directory back to the original one
      os.chdir(self.prev_dir)

      # Remove the temporary directory and its contents
      shutil.rmtree(self.temp_dir)


with TempDir() as temp_dir:
    # Inside this block, temp_dir is the path to the temporary directory
    print(f"Current working directory: {os.getcwd()}")  # Output: Path to the temporary directory

# Outside the block, the temporary directory has been removed and the working directory is back to its original state
print(f"Current working directory: {os.getcwd()}") 