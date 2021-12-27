import {LitElement, html,css} from 'lit';
import {customElement, property} from 'lit/decorators.js';
import '@polymer/paper-item/paper-item';
import '@polymer/paper-tabs/paper-tab';
import '@polymer/paper-tabs';
import './evComp.js'


class Main extends LitElement {
    //define styles separttely
      static styles = css`
      .tabcontent {
        color: green;
        display: none;
      }
      paper-tabs{
        --paper-tabs-selection-bar-color : #4286f4;
        background-color:green;
      }
      paper-tab {
        border: 1px solid yellow;
      }
      paper-tab.iron-selected {
        color: blue;
        background-color: lightblue
      }
    `;

    // Define a template
    myTemplate = (title)=> html`
    <div id="header">
    <div style="width:10em;margin:auto;background-color:lightblue;font-weight:bold">
    <paper-item class="hdr">EV Car models</paper-item>
    </div>
    <!-- These are tabs (a horizontal row of buttons) -->
    <paper-tabs>
      <paper-tab class="tablinks" @click="${this.openTab}">Tesla EV</paper-tab>
      <paper-tab class="tablinks" @click="${this.openTab}">Toyota EV</paper-tab>
      <paper-tab class="tablinks" @click="${this.openTab}">Solo EV</paper-tab>
      <paper-tab class="tablinks" @click="${this.openTab}">Hyundai EV</paper-tab>
    </paper-tabs>
    </div>
    <!-- The tab content area -->
    <div style="padding-top: 6em;">
    <!-- Tab content -->
    <div class="tabcontent">
      <ev-comp title="Tesla EV"></ev-comp>
    </div>

    <div class="tabcontent">
      <ev-comp title="Toyota EV"></ev-comp>
    </div>

    <div class="tabcontent">
    <ev-comp title="Solo EV"></ev-comp>
    </div>

    <div class="tabcontent">
    <ev-comp title="Hyundai EV"></ev-comp>
    </div>

    </div>
    `;
    //property changes will cause render to be called again
    static get properties() {
      return {
        loadStatus: { type: String }
      };
    }
    constructor() {
      super();
      this.loadStatus='loaded'  //This is used to trigger rendering of page after the response from config service
    }

  async passConfigInfoToChildren(passConfigTo,config){
    //wait for child components to be available and pass on the config info
    for (const childComp of passConfigTo) {
      await childComp.updateComplete
      if (typeof(childComp.receiveConfigInfo)==='function') await childComp.receiveConfigInfo(config)
    }
  }

  async firstUpdated(changeProperties){
    let config =  {
      'Toyota EV':{
        'imgUrl':'https://toyota.scene7.com/is/image/toyota/BZ4_MY23_0018_V001-1?fmt=jpg&fit=crop&resMode=bisharp&qlt=90&wid=1696&hei=952'
      },
      'Tesla EV':{
        'imgUrl':'https://www.thedrive.com/content/2021/12/0x0-Model3_26.jpg?quality=85&width=1440&quality=70'
      },
      'Solo EV':{
        'imgUrl':'https://electrek.co/wp-content/uploads/sites/3/2016/08/solo-2.jpg?quality=82&strip=all'
      },
      'Hyundai EV':{
        'imgUrl':'https://cdn.vox-cdn.com/thumbor/_YuMe2L1LW7RNi-f8eHCKDdu_zs=/0x0:3395x2147/920x613/filters:focal(1427x803:1969x1345):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/70155884/48639_HyundaiMotorUnveilsSEVENConceptSegment_bustingSUEVfortheIONIQBrand.0.jpg'
      }
    }
    //get the children to whom we want to pass the config-info
    let passConfigTo = this.shadowRoot.querySelectorAll('ev-comp')
    //let config="first content"
    this.passConfigInfoToChildren(passConfigTo,config)
  }

  async openTab(e) {
    let activeTabNm = e.target.innerText //name of the tab clicked
    console.log(`Clicked on ${activeTabNm}`);
    let activeTabDiv=this.shadowRoot.querySelector('ev-comp[title="'+activeTabNm+'"'+']').closest(".tabcontent")
    // Get all tab content divs and hide them
    let tabcontent = this.shadowRoot.querySelectorAll(".tabcontent");
    for (let i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    // Show the current tab, and add an "active" class to the button that opened the tab 
    activeTabDiv.style.display = "block";
  }

  render() {
      if (this.loadStatus == 'loading') return html`loading configs..`
      else {
        return this.myTemplate("Sms 0.0");
    }
  }
}
customElements.define('main-comp',Main)