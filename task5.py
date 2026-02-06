pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/ssowmiya2206/pipeline1.git'
 }
 }
 stage('Read File') {
 steps {
 bat 'type README.md'
 }
 }
 }
}
