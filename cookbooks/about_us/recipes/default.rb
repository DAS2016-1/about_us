#packages needed
execute 'apt-get update'
package 'vim'
package 'python-debian'
package 'python3-pip'
execute 'pip3 install -r requirements.txt'

