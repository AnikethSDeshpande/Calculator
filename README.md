# Calculator
Learning Git Commands

This repository is for me personal use.. to learn git commands

1. **Reset** Head (--soft: commit cancelled, code back to staging area, 
2.             --mixed(default): commit cancelled, code back to woeking area
3.             --hard: commit cancelled, code lost from both staging and working areas
4.            )
5. **Revert** Head: changes in the past commit is deleted and a new commit is created which is ahead of the last commit. (helpful for pushing code as the commits aren't missed)
6. **Rebase**: (git rebase -i HEAD~3) 
            use rebase to **squash** commits into one sensible commit per feature. helps reduce the number of redundant commits.
          
