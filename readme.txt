https://www.youtube.com/watch?v=tl2eEBFEHqM

1. make sure to have pyenv-win. else, install pyenv.
install pyenv-win using powershell https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#git-commands

2. "pyenv install 3.10.11"

3.  "pyenv global 3.10.11"

4. "pip install virtualenv"

5. if not yet present (if you did not download the wholre repo), create virtual environment "python -m venv face_rev_v1_env"

6. activate the virtual environment by ".\face_rec_v1_env\Scripts\activate". this is to prevent some possible conflicts with some python library and python version compatibility

7. install visual studio code for c++. this may take a while. like 4GB to 5GB of download.
8. download cmake https://cmake.org/download/ , use the msi installer. and dont forget to add "add to path for all users"

10. pip install dlib

8. "pip install opencv-python"

9. "pip install face_recognition"

10. put images in .png format in the /faces folder. make sure they are named correctly. remove spaces if possible to prevent bugs in the code.

11. run "python main_not.py"


what did i do?
1. i used pyenv to ensure correct python version. this is for the compatibililty of external python libraries
2. we did "pip install virtualenv" to reate a virtual python environment to make sure there is no clash in unexpected currently installed other software or python library
3. other software and compilers we neede was visual studio with c++ support and cmake. these are just for compiling the extracted data from the images fed to the python software.
4. dlib -> pasuyo ng google, opencv -> very famous. opensource computer vision library. face_recognition yung mismong core library of thiss project.
5. to use, put the images in the faces folder. and run "python .\my_main_program.py
