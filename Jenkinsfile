pipeline{
  agent any
  stages{
    stage('Ansible Install & Verify (Also installs docker)'){
      steps{
        sh "bash jenkins/scripts/ansibleinstallverify.sh"
      }
    }
    stage('Testing'){
      steps{
        sh "bash jenkins/scripts/testing.sh"
      }
    }  
    stage('Stack Set-up'){
      steps{
        sh "bash jenkins/scripts/stacksonstacks.sh"   
      }
    }
  }
}