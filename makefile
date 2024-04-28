local:
	chalice local

deploy:
	aws cloudformation create-stack \
  	--stack-name myteststack \
  	--template-body cloudformation/mysql.yml
