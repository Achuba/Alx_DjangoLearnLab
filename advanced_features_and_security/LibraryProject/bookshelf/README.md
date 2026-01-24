# The 'Book' model has custom permissions: can_view, can_create, can_edit, can_delete

# Groups:

# - Editors: can_create, can_edit

# - Viewers: can_view

# - Admins: all permissions

# Use @permission_required decorator in views to enforce these permissions.
