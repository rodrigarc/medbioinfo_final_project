# basic statistics and plot

# Run the analysis
results : src/plot_protein-interaction-vs-domains.py data envir data/proteins_w_domains.txt data/9606.protein.links.v11.0.txt.gz 
	python $<

# Download data with python script from the protein interactions
envir: environment.yml
	conda env create --file=$<
	conda activate medbioinfo
data : 9606.protein.links.v11.0.txt.gz data/proteins_w_domains.txt envir
9606.protein.links.v11.0.txt.gz : src/download_data.py envir
	python $<

.PHONY : clean
clean :
	rm -f results/*.csv results/*.png