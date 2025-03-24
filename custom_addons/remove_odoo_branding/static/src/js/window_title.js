/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

registry.category("services").add("title_service", {
    dependencies: [],
    start() {
        document.title = "CloudERP";
    },
});
