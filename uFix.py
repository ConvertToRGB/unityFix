#! python2
# -*- coding: utf-8 -*-


'''import modules'''

import os
import sys
import json


'''find file in directory and return full path of the found file'''

def findFile(root, myFile):
    fileWasFound = ""
    tree = os.walk(root)

    for i in tree:
        for j in i[2]:
            if j == myFile:
                fileWasFound = u"File was found"
                fileToFixFullNameFound = os.path.join(os.path.abspath(i[0]),j)
    
    if fileWasFound:
        print fileWasFound
        return fileToFixFullNameFound
    else:
        print u"File was not found".encode("cp866")
        return 0


'''define variables'''

uFixFullName = sys.argv[0].decode("cp1251")
uFixDirName = os.path.dirname(uFixFullName)
jsonFileName = u"unityFixSettings.json"
fileToFixName = u"CurrentLayout-default.dwlt"
jsonSettingsFilePath = os.path.join(uFixDirName, jsonFileName)
contentToJson = {}


'''check if we have json file settings or not
if yes, we load them, if not, we ask user some data
and then create json settings file if data is correct'''

if os.path.exists(os.path.join(uFixDirName, jsonFileName)):
    correctFileProcess = False
    contentFromJson = json.load(open(jsonSettingsFilePath))
    for k in contentFromJson:
        if k == u"delete":
            if os.path.exists(contentFromJson[k]):
                os.remove(contentFromJson[k])
            else:
                print "File to delete is missing!".encode("cp866")
        elif k == u"correctFile":
            correctDwltFile = contentFromJson[k]
            correctFileProcess = True
        elif k == u"toFix":
            fileToFixFullName = contentFromJson[k]
            correctFileProcess = True
    if correctFileProcess:
        if os.path.exists(correctDwltFile) and os.path.exists(fileToFixFullName):
            if os.path.isabs(correctDwltFile) and os.path.isfile(correctDwltFile):
                dwltFile = open(correctDwltFile, "r")
                dwltContent = dwltFile.readlines()
                dwltFile.close()

                rewriteDwltFile = open(fileToFixFullName, "w")
                rewriteDwltFile.writelines(dwltContent)
                rewriteDwltFile.close()
        else:
             print "Files to fix are missing!".encode("cp866")
    print "Done!".encode("cp866")

else:
    '''ask user if he has correct dwlt file'''

    correctDwlt = raw_input("Do you have correct *.dwlt file? [y/n] ").decode("cp866")


    '''if user has correct dwlt file, then we ask him to put it here and then we use data from
    correct file to overrite corrupted file'''

    if correctDwlt.lower() == u'y': 
        correctDwltFile = raw_input("Enter path to correct *.dwlt file: ").decode("cp1251")
        correctDwltFile = correctDwltFile.lstrip("&").strip().strip('"')
        if os.path.exists(correctDwltFile) and os.path.isfile(correctDwltFile):
            dwltFile = open(correctDwltFile, "r")
            dwltContent = dwltFile.readlines()
            dwltFile.close()

            fileToFixFullName = findFile(uFixDirName, fileToFixName)
            rewriteDwltFile = open(fileToFixFullName, "w")
            rewriteDwltFile.writelines(dwltContent)
            rewriteDwltFile.close()

            contentToJson["correctFile"] = correctDwltFile
            contentToJson["toFix"] = fileToFixFullName 
            json.dump(contentToJson, open(jsonSettingsFilePath, 'w'), indent=4)

        else:
            print u"wrong path"

    else:
        '''if user doesn't have correct file, then we just delete corrupted file and do nothing more'''

        fileToDelete = findFile(uFixDirName, fileToFixName)
        if fileToDelete:
            if os.path.exists(fileToDelete):
                os.remove(fileToDelete)
            contentToJson["delete"] = fileToDelete
            json.dump(contentToJson, open(jsonSettingsFilePath, 'w'), indent=4)
        else:
            print u"File 'CurrentLayout-default.dwlt' was not found".encode("cp866")


raw_input()