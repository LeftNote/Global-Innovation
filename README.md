Global-Innovation
=================

gloinno.com
[ ![Codeship Status for LeftNote/Global-Innovation](https://codeship.com/projects/eaf84850-84f0-0132-ef94-6ae5548b2deb/status?branch=master)](https://codeship.com/projects/58575)

Git Workflow Guideline
======================

For version control, Global Innovation uses a simplified version of the famous [Gitflow Workflow](https://www.atlassian.com/git/workflows#!workflow-gitflow), (you can read the original article [here](http://nvie.com/posts/a-successful-git-branching-model/)). 

Master Branch
-------------
Master branch will be the main branch to develop on. Master branch should only keep commits directly related to JIRA.

- **Branch off: feature**

- Each commit corresponds to an issue, must mention issue number in the commit, eg. `JIRA: RC-3`
- Branch off into feature branches

Feature Branches
-------------
A feature branch is created to address one big feature that multiple developers may need to collaborate on. This is different from a local branch in that a feature branch is eventually merged as is to a master branch. It can be thought as an alternative buffer for master when a feature takes very long to implement. 

- **Merge into: master**
- Each commit corresponds to an issue, must mention issue number in the commit, eg. `JIRA: RC-3`
- **Branch off: none**


Scenarios
-------------
### Start Working on a New Issue/Feature branch
Make sure master is up-to-date

        git checkout master
        git pull --ff-only

Branch off the newest master

        git checkout -b <issue-name> origin/master

It is important to set the upstream to `origin/master` so you can see how ahead/behind your branch is. Replace `<issue-name>` with your feature/bug/fix name. This is a local branch and should only exist on your VM. If the issue is long-running or needs multiple collaborators, consider creating a feature branch by prefixing `feature-` to the branch name and pushing it to `origin`.

### Merge a Completed Issue/Feature Branch
Make sure master is up to date

        git checkout master
        git pull --ff-only

If the master is now ahead of your local branch (`git branch -vv` to see status of each branch), merge Master into your feature branch first before merging it back to Master.

        git co <issue-name>
        git merge master
        # fix conflict if any
        git co master

Now merge-squash your branch if your branch is a local, short-lived issue branch

        git merge --squash <issue-name>

If the branch is a feature branch, do not use Merge-Squash. All the commits inside a feature branch will need to show up on master.

        git merge <feature-branch>

Then, 

        git status

Examine and make sure the changes are expected

        git commit

For the commit message, follow this template

        <present-tense-third-person-verb> <message>

        JIRA: <jira-issue-number>
        Reviewer: <code-reviewer>

An example would be:

        Finishes implementing picture uploading feature.

        JIRA: RC-3
        Reviewer: Donny