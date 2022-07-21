from openupgradelib import openupgrade

namespec = [("project_deadline", "project")]


@openupgrade.migrate()
def migrate(cr, env, version):
    openupgrade.update_module_names(cr, namespec, False)
