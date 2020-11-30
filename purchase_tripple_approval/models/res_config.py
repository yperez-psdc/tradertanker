## -*- coding: utf-8 -*-

#from odoo import fields, models, api


#class PurchaseConfigSettings(models.TransientModel):
##     _inherit = 'purchase.config.settings'
#    _inherit = 'res.config.settings'

#    three_step_validation =  fields.Boolean(
#        'Three Step Approval'
#    )
#    finance_validation_amount = fields.Monetary(
#        'Finance Validation Amount',
#        default=0.0
#    )
#    director_validation_amount = fields.Monetary(
#        'Director Validation Amount',
#        default=0.0
#    )
#    email_template_id = fields.Many2one(
#        'mail.template',
#        string='Purchase Approval Email Template',
#    )
#    refuse_template_id = fields.Many2one(
#        'mail.template',
#        string='Purchase Refuse Email Template',
#    )

#    @api.model
#    def get_values(self):
#        res = super(PurchaseConfigSettings, self).get_values()
#        params = self.env['ir.config_parameter'].sudo()
#        res.update(
#            three_step_validation = params.get_param('purchase_tripple_approval.three_step_validation'),
##             finance_validation_amount = params.get_param('purchase_tripple_approval.finance_validation_amount'),
##             director_validation_amount = params.get_param('purchase_tripple_approval.director_validation_amount'),
##             email_template_id = params.get_param('purchase_tripple_approval.email_template_id'),
##             refuse_template_id = params.get_param('purchase_tripple_approval.refuse_template_id')
#        )
#        if self.email_template_id:
#            res.update(
#            email_template_id = params.get_param('purchase_tripple_approval.email_template_id'),
#        )
#        return res

#    #@api.multi
#    def set_values(self):
#        super(PurchaseConfigSettings, self).set_values()
#        ICPSudo = self.env['ir.config_parameter'].sudo()
#        ICPSudo.set_param("purchase_tripple_approval.three_step_validation", self.three_step_validation)
##         ICPSudo.set_param("purchase_tripple_approval.finance_validation_amount", self.finance_validation_amount)
##         ICPSudo.set_param("purchase_tripple_approval.director_validation_amount", self.director_validation_amount)
#        if self.email_template_id:
#            ICPSudo.set_param("purchase_tripple_approval.email_template_id", self.email_template_id)
##         ICPSudo.set_param("purchase_tripple_approval.refuse_template_id", self.refuse_template_id)








##     @api.model
##     def get_default_three_step_validation(self, fields):
##          return {'three_step_validation': self.env['ir.values'].get_default(
##                  'purchase.config.settings', 'three_step_validation')}
## 
##     @api.model
##     def set_default_three_step_validation(self):
##          config_value = self.three_step_validation
##          self.env['ir.values'].set_default('purchase.config.settings', 'three_step_validation', config_value)
## 
##     @api.model
##     def get_default_finance_validation_amount(self, fields):
##          return {'finance_validation_amount': self.env['ir.values'].get_default(
##                  'purchase.config.settings', 'finance_validation_amount')}
## 
##     @api.model
##     def set_default_finance_validation_amount(self):
##          config_value = self.finance_validation_amount
##          self.env['ir.values'].set_default('purchase.config.settings', 'finance_validation_amount', config_value)
## 
##     @api.model
##     def get_default_director_validation_amount(self, fields):
##          return {'director_validation_amount': self.env['ir.values'].get_default(
##                  'purchase.config.settings', 'director_validation_amount')}
## 
##     @api.model
##     def set_default_director_validation_amount(self):
##          config_value = self.director_validation_amount
##          self.env['ir.values'].set_default('purchase.config.settings', 'director_validation_amount', config_value)
## 
##     @api.model
##     def set_default_email_template_id(self):
##          config_value = self.email_template_id.id
##          self.env['ir.values'].set_default('purchase.config.settings', 'email_template_id', config_value)
## 
##     @api.model
##     def get_default_email_template_id(self, fields):
##          return {'email_template_id': self.env['ir.values'].get_default(
##                  'purchase.config.settings', 'email_template_id')}
## 
##     @api.model
##     def get_default_refuse_template_id(self, fields):
##          return {'refuse_template_id': self.env['ir.values'].get_default(
##                  'purchase.config.settings', 'refuse_template_id')}
## 
##     @api.model
##     def set_default_refuse_template_id(self):
##          config_value = self.refuse_template_id.id
##          self.env['ir.values'].set_default('purchase.config.settings', 'refuse_template_id', config_value)

## vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
