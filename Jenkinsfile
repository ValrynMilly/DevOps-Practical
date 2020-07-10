pipeline{
  agent any
  stages{
    stage('Docker Stack'){
      steps{
        sh "bash jenkins/scripts/stacksonstacks.sh"   
      }
    }
  }
}