local:
	chalice local

sync_static:
	aws s3 sync ./static s3://cloudfront-dofus-trade/ --delete
	aws cloudfront create-invalidation --distribution-id E3C3V1X0LMI8L3 --paths "/app.css"