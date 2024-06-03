/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.SchoolCourse = publicWidget.Widget.extend({
    selector: '.school-course',
    start() {
        //console.log("START 123")
        //console.log(this)
        //console.log(this.el)
        //console.log(this.el.querySelector('#school-course-row'))

        let coursesRow = this.el.querySelector('#school-course-row')
        //console.log("-->"+coursesRow)

        if (coursesRow){
            this._rpc({
                route: '/courses-json/',
                params:{}
            }).then(data=>{
                let html = ``
                data.forEach(course=>{
                    html += `<div class="col-6">
                                <div class="course-container d-flex flex-row shadow mb-5 br-3">
                                    <div class="col-4">
                                    <a href="#"><img src="data:image/jpg;base64,${course.introimage}"
                                            class="d-block w-100 rounded-w2" alt="cover 1"/></a>
                                    </div>
                                    <div class="col-8 d-flex justify-content-center align-items-center p-3">
                                        <h3><a href="#">${course.name}</a></h3>
                                    </div>
                                </div>
                             </div>`
                })

                coursesRow.innerHTML = html
            })
        }
    },
});

export default publicWidget.registry.SchoolCourse;
