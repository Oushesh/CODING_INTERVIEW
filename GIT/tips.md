### if your head is by 1 commit ahead and you by accident committed big files
    * Do soft reset first
      git reset --soft HEAD~1
    * All files will be uncommited and restaged and git status will show them as green
      See through them and the ones you wanna unstage:
      git reset "Desired Folder"
