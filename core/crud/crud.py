from . import user, geoAddress, ai 

# User CRUD 
get_user = user.get_user
get_user_by_email = user.get_user_by_email
get_users = user.get_users
delete_user = user.delete_user
update_user = user.update_user
patch_user = user.patch_user
create_user = user.create_user

# GeoAddress CRUD 
create_geoAddress = geoAddress.create_geoAddress
update_geoAddress = geoAddress.update_geoAddress


# Propostion CRUD 
create_ai = ai.create_ai
# get_ais = ai.get_ais
# get_ais_request = ai.get_ais_request
# get_ai = ai.get_ai
# delete_ai = ai.delete_ai
