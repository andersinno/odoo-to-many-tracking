from odoo import api, models


class MailTracking(models.Model):
    _inherit = "mail.tracking.value"

    @api.model
    def create_tracking_values(
        self,
        initial_value,
        new_value,
        col_name,
        col_info,
        tracking_sequence,
        model_name,
    ):
        result = super().create_tracking_values(
            initial_value=initial_value,
            new_value=new_value,
            col_name=col_name,
            col_info=col_info,
            tracking_sequence=tracking_sequence,
            model_name=model_name,
        )
        if result:
            return result

        field = self.env["ir.model.fields"]._get(model_name, col_name)
        if field and col_info["type"] in ["many2many", "one2many"]:

            def to_string(records):
                names = [x.sudo().name_get()[0][1] for x in records]
                return ", ".join(names)

            return {
                "field": field.id,
                "field_desc": col_info["string"],
                "field_type": col_info["type"],
                "tracking_sequence": tracking_sequence,
                "old_value_char": to_string(initial_value),
                "new_value_char": to_string(new_value),
            }

        return result
