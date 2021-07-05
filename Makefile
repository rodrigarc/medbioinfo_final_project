# basic statistics and plot

# Run the analysis
results : src/plot_protein-interaction-vs-domains.py data data/proteins_w_domains.txt data/9606.protein.links.v11.0.txt.gz 
	python $<

# Download data with python script from the protein interactions
#envir: environment.yml
#	conda env create --file=$<
data : 9606.protein.links.v11.0.txt.gz data/proteins_w_domains.txt
9606.protein.links.v11.0.txt.gz : src/download_data.py 
	python $<

.PHONY : clean
clean :
	rm -f results/*.csv results/*.png