git add .;
read -p "Enter commit message: " message;
git commit -m "$message";
git push origin main;
echo "Commit pushed to origin main";
