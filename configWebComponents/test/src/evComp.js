import {LitElement, html} from 'lit';
import {customElement, property} from 'lit/decorators.js';


class EvComp extends LitElement {
    myTemplate = ()=> html`
    <div id="config">
    </div>
    `;

    constructor() {
        super();
    }

    async receiveConfigInfo(config) {
        this.shadowRoot.querySelector("#config").innerHTML=config
        let imgUrl=config[this.title].imgUrl
        this.shadowRoot.querySelector("#config").innerHTML=`<img src="${imgUrl}" />`
    }
    render() {
          return this.myTemplate();
    }
}
customElements.define('ev-comp',EvComp)