from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website, QueryURL



class main(http.Controller):


    # START CONTENT TYPE (portal) - documents ----------------------------------------------------
    @http.route(['/documents', '/documents/page/<int:page>'], auth="public", website=True)
    def website_documentsListView(self, page=1, **kw):
        document_obj = http.request.env['school.document']
        total_documents = document_obj.search_count([])
        page_detail = request.website.pager(url='/documents',
                                            total=total_documents,
                                            page=page,
                                            step=5)

        documents = document_obj.search([], limit=5, offset=page_detail['offset'])
        vals = {'documents': documents, 'page_name': 'documents_list_view', 'pager': page_detail}
        return http.request.render('theme_web2e.template_documents_list_view_portal', vals)

    @http.route(['/documents/<model("school.document"):document_id>'], type="http", website=True)
    def website_documentsFormView(self, document_id, **kw):
        vals = {'document': document_id, 'page_name': 'documents_form_view'}
        document_records = request.env['school.document'].search([])
        document_ids = document_records.ids
        document_index = document_ids.index(document_id.id)
        if document_index != 0 and document_ids[document_index - 1]:
            vals['prev_record'] = '/documents/{}'.format(document_ids[document_index - 1])
        if document_index < len(document_ids) - 1 and document_ids[document_index + 1]:
            vals['next_record'] = '/documents/{}'.format(document_ids[document_index + 1])

        return http.request.render('theme_web2e.template_documents_form_view_portal', vals)

    # END CONTENT TYPE (portal) - documents ----------------------------------------------------


    # STARAT - customers  https://www.cybrosys.com/blog/how-to-add-pagination-odoo-website  ----
    # 1.SERP
    @http.route(['/customers', '/customers/page/<int:page>'], type="http", auth="user", website=True)
    def website_customers(self, page=0, search='', **post):
        domain = []
        if search:
            domain.append(('name', 'ilike', search))
        if search:
            post["search"] = search
        customer_obj = request.env['res.partner'].sudo().search(domain)
        total = customer_obj.sudo().search_count([])
        pager = request.website.pager(
            url='/customers',
            total=total,
            page=page,
            step=3,
        )

        offset = pager['offset']
        customer_obj = customer_obj[offset: offset + 5]

        vals = {
            'search': search,
            'customers': customer_obj,
            'pager': pager
        }

        return http.request.render('theme_web2e.template_list_customers_page', vals)

    # 2.DETAIL
    @http.route('/customer/<model("res.partner"):customer>', auth='public', website=True)
    def website_course(self, customer):
        return http.request.render('theme_web2e.template_form_customer_page', {
            'customer': customer
        })
    # END - customers  https://www.cybrosys.com/blog/how-to-add-pagination-odoo-website  ----
