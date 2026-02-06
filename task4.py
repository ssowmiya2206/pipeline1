pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/ssowmiya2206/pipeline1.git'
 }
 }
 stage('Create File') {
 steps {
 bat 'echo This file is created by Jenkins > demo.txt'
 }
 }
 }
}
