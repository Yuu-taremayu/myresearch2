#! /bin/zsh

source ~/.zshrc

if [ $# -eq 1 ]; then
	FILE1="secret.hex"
	if [ -e $1 ]; then
		xxd -p $1 > ${FILE1}
		echo "Succeeded convert to hex."
	else
		echo "Error occurred.(1)"
	fi

	if [ -e ${FILE1} ]; then
		time /home/yu_pippi/.pyenv/versions/3.7.9/bin/python3 /home/yu_pippi/myresearch2/program/AdditiveSecretSharing/AdditiveSecretSharing.py ${FILE1}
		echo "Succeeded Secret Sharing."
	else
		echo "Error occurred.(2)"
	fi

	FILE2="secret_reconst.hex"
	FILE3="secret_reconst.txt"
	if [ -e ${FILE2} ]; then
		touch ${FILE3}
		xxd -p -r ${FILE2} > ${FILE3}
		echo "Succeeded convert to text."
	else
		echo "Error occurred.(3)"
	fi

	if [ -e ${FILE3} ]; then
		diff -s $1 ${FILE3}
		echo "Succeeded reconstruct."
	else
		echo "Error occurred.(4)"
	fi

	ls -la | grep 'Share' | cut -d ' ' -f 5 > sharesize_sum.txt
	awk '{ s += $size }; END { print "sum="s"[KB],", "average="s/NR"[KB]"}' < sharesize_sum.txt
else
	echo "usage: ./ASS.sh [file]"
fi
