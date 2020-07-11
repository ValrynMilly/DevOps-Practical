pipeline{
  agent any
  stages{
    stage('Stack Set-up'){
      steps{
        sh "bash jenkins/scripts/stacksonstacks.sh"   
      }
    }
    stage('Ansible Install & Verify'){
      steps{
        sh "bash Jenkins/scripts/ansibleinstallverify.sh"
      }
    }
  }
}