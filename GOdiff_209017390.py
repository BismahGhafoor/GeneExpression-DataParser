## A SCRIPT THAT CREATES A TSV FILE THAT CONTAINS THE NAME, DESCRIPTION AND P-VALUE OF EACH SIGNIFICANTLY EXPRESSED  GENE IN THE GO CATEGORY: GO0003723 THAT IS DIFFERENTIALLY EXPRESSED AND PRINTS THE GENE WITH THE LOWEST P-VALUE (last modified - 23.10.2023)

# Open the two files for reading
genelist = open("GO0003723.genelist", "r")
diffexp = open("diffexp.tsv", "r")

# Create an empty dictionary for the genelist
genelist_dict = {}

# Create a for loop to append to the genename and gene description to the genelist dictionary
for line in genelist:
	line = line.split("\t") # The information is in tab seperated format so we sperate using '\t'
	genelist_dict[line[3]] = line[4] # This is telling the for loop to append the description of the gene (which will be the value) to each gene name (which will be the key)
genelist.close()

# Create a second empty dictionary to append the gene name and their p-values from the diffexp data file
diffexp_dict = {}

# Create a for loop for the second file to append the key (gene name) and values (p-values) to the dictionary
for line in diffexp:
	line  = line.split("\t")
	pvalue = float(line[4]) # Float() function is used to allow comparisons of the numbers
	if pvalue < 0.05: # We are only interested in the differentially expressed genes so we are only appending the genes with a p-value less than 0.05 to the dictionary
		diffexp_dict[line[0]] = float(pvalue)
diffexp.close()

# Create an empty list to store the p-values
pvalue_list = []

# Write the tab seperated output file that prints the gene name, description and p-value
with open("GOdiff_209017390.out", "w") as f:
	f.write("genename\tdescription\tpvalue\n")
	for gene in diffexp_dict:
		if gene in genelist_dict: # This is used because the genelist_dict contains the gene names for all of the genes in the GO category: GO0003723
			f.write(gene + "\t" + genelist_dict[gene] + "\t" + str(diffexp_dict[gene]) + "\n") # str() function is used on the pvalue because you cant concatenate strings with a float, they all need to be strings
			pvalue_list.append(float(diffexp_dict[gene])) # Appending the p-value to the pvalue-list that will be used to find the minimum pvalue later

# Find the minimum p-value
minvalue = pvalue_list[0]

for pvalue in pvalue_list:
	if pvalue < minvalue: # If the pvalue is less than the minvalue value then...
		minvalue = pvalue # ... Assign this pvalue to the minvalue variable

#For-loop to find the gene with the lowest p-value
for key, value in diffexp_dict.items():
	if value == minvalue:
		print("The gene with the lowest p-value is " + key + " with the p-value " + str(value))
