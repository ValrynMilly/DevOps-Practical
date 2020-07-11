pipeline{
  agent any
  stages{
    stage('Ansible Install & Verify'){
      steps{
        sh "bash jenkins/scripts/ansibleinstallverify.sh"
      }
    }  
    stage('Stack Set-up'){
      steps{
        sh "bash jenkins/scripts/stacksonstacks.sh"   
      }
    }
  }
}