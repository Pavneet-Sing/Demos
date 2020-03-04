<h1 align="center">Steps to setup git repo</h1>

Setup git repo environment:
--------------------------

1. Setup user details

        git config --global user.name "Your name here"
        git config --global user.email "your_email@example.com"

2. Generate SSH key(skip to next step to reuse existing ssh key) 
      
      a.) For Mac . ([Read more about SSH keys](https://www.ssh.com/ssh/keygen))

		ssh-keygen -t rsa -C "your_email@example.com"
      b.)  Copy SSH key

		pbcopy < ~/.ssh/id_rsa.pub
   For Windows,
   
      a.) Either use [putty.exe](https://www.putty.org) or open git bash and type
	    
	      ssh-keygen -t rsa
    
    then look under `your_home_directory/.ssh/id_rsa.pub ` path and open `id_rsa.pub` file then copy(excluding spaces) the content(SSH key)

3. Add SSH key to account

    a.) Go to https://github.com/settings/profile
	
    b.) Open SSH key section or use https://github.com/settings/ssh
	 
    c.) Paste your key and save it
    ![github-ssh](https://user-images.githubusercontent.com/11755381/75902679-686efa00-5e66-11ea-9583-d27fb8ab3fec.png)

Setup local repo for new project:
--------------------------------
1. Setup new repository

     	git init

2. Create `.gitignore` file(for new repo) and add content from [.gitignore android file](https://github.com/github/gitignore/blob/master/Android.gitignore), Optionally can create and add `README.md` for project documentation 

3. Add file(s) to staging using (use `git status` to view the staged/unstaged changes)

		git add path/filename
   or add all files using

		git add .

4. Commit the previously staged changes

		git commit -m "init repo message"

5. Push changes to remote repo

	a) Create a new project under github/gitlab/bitbucket account, etc and copy the SSH-link

		git remote add origin https://github.com/UserName/RepoName.git

	b) Pull auto generated license or README file
	
	**Caution**: use `--allow-unrelated-histories` only once for new repo to pull license, README files.

		git pull origin master --allow-unrelated-histories

	c) Push code

		git push origin master


Setup local repo using clone:
-----------------------------------
1. Clone existing project from github using

   	 	git clone SSH-link.git
   ![ssh_link](https://user-images.githubusercontent.com/11755381/75903716-fd262780-5e67-11ea-873d-bdc4377da81a.png)

2. Add file(s) to staging using

		git add path/filename
   or add all files using

		git add .
3. Commit the previously staged changes

		git commit -m "init repo message"
4. Push changes to remote repo

	a) In case of new repo, make sure to create a project under github/gitlab/bitbucket account etc and copy the SSH-link

		git remote add origin https://github.com/UserName/RepoName.git
	Push code

		git push origin master

Pull Sub-module
---------------
For large repositories with submodules, it's recommended to update them recursively as:

    git submodule update --init --recursive