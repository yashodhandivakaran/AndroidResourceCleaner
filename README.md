# AndroidResourceCleaner
This is a simple  python script which takes the path of lint-result xml file and removes all the unused files from the project.

#How to use it:

### Android Lint 
To generate lint report:

* Go to your Android project directory and execute the lint task
```sh
$ ./gradlew lint
```
* Once this command execution is completed, it will generate report in html and xml file into <YOUR_PROJECT>/build/output

### Android Resource Cleaner script

* Once you are done with generating lint report execute the script with the xml report file as input
```sh
$ ./android_resource_cleaner.py -i ~/<PROJECT_PATH>/build/outputs/lint-results.xml
```
* This will clear all the resource files which are not used in your project as per lint.
* To see all the files which are delete go to android_resource_cleaner_output.txt file, this file will be created in the directory where this script is present.



