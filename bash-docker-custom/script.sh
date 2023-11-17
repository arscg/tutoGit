# Vérifiez si le nombre d'arguments est correct
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <prenom> <nom>"
    exit 1
fi

# Récupérez les arguments
prenom=$1
nom=$2

# Affichez le message
echo "Hello, $prenom $nom!"
