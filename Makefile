# basic statistics and plot

# Run the analysis
results : data data/proteins_w_domains.txt data/9606.protein.links.v11.0.txt.gz src/plot_protein-interaction-vs-domains.py
	python src/plot_protein-interaction-vs-domains.py 

# Download data with python script from the protein interactions
data : 9606.protein.links.v11.0.txt.gz data/proteins_w_domains.txt
9606.protein.links.v11.0.txt.gz : src/download_data.py 
	python src/download_data.py

.PHONY : clean
clean :
	rm -f results/*.csv results/*.png