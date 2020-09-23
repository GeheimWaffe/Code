Objectif : exécuter protractor

*** Setup

d'abord installer protractor
npm install -g protractor

Puis tester l'update de webdriver
webdriver-manager update

Et enfin démarrer un serveur avec webdriver
webdriver-manager start

*** Pour installer et configurer Selenium
* D'abord installer selenium en tant que tel
pip install Selenium

* Puis configurer un répertoire où placer les exécutables
* se placer à la racine Puis
cd opt
sudo mkdir webdriver
sudo mkdir bin

* Puis télécharger le geckodriver sur GitHub
* et exécuter la copie pour l'envoyer vers le répertoire cible
sudo cp geckodriver /opt/WebDriver/bin
