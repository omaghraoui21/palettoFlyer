const fs=require('fs'),vm=require('vm'),assert=require('assert'),crypto=require('crypto');
const root=require('path').resolve(__dirname,'../..')+'/',html=fs.readFileSync(root+'comparaison-ultibro/COMPARATIF_TROIS_METHODES.html','utf8');
const dataText=html.match(/<script id="source-data" type="application\/json">([\s\S]*?)<\/script>/)[1],data=JSON.parse(dataText),code=html.match(/<script>\n([\s\S]*?)<\/script>/)[1];
const nodes={};for(const m of html.matchAll(/<([a-z0-9-]+)\b([^>]*\bid="([^"]+)"[^>]*)>/g)){const attrs=m[2],id=m[3];nodes[id]={tag:m[1],value:(attrs.match(/\bvalue="([^"]*)"/)||[])[1]||'',textContent:'',_html:'',disabled:false,addEventListener(){},classList:{toggle(){}},scrollIntoView(){},appendChild(){}};Object.defineProperty(nodes[id],'innerHTML',{get(){return this._html},set(s){this._html=s;if(this.tag==='select'){const v=s.match(/<option value="([^"]*)"/);if(v)this.value=v[1]}}});}
for(const m of html.matchAll(/<select\b[^>]*id="([^"]+)"[^>]*>([\s\S]*?)<\/select>/g))nodes[m[1]].innerHTML=m[2];nodes['source-data'].textContent=dataText;
const document={getElementById(id){if(!nodes[id]){nodes[id]={innerHTML:'',textContent:'',value:''}}return nodes[id]},addEventListener(){},createElement(){return {click(){},remove(){}}},body:{appendChild(){}}};
const ctx={document,window:{},console,setTimeout:()=>{},Blob,Uint8Array,atob,URL};vm.createContext(ctx);vm.runInContext(code,ctx,{timeout:3000});
assert.equal(data.astra.length,19);assert.equal(data.fable.length,15);assert.equal(data.experiments.length,16);assert.equal(data.power.length,72);
for(const d of data.docs){const b=Buffer.from(d.data,'base64');assert.equal(crypto.createHash('sha256').update(b).digest('hex'),d.sha256);assert(b.equals(fs.readFileSync(root+d.path)));}
const base={batch:300,fill:25,ind:100,gly:100,mg:.15,mode:'pct',fines:0,ml:100,min:null};
for(const [name,e] of Object.entries(data.checks.exemples_theoriques)){const r=ctx.window.calculateM3({...base,fines:name==='M3-F3'?3:name==='M3-F6'?6:0,ml:name==='M3-C'?50:100});Object.values(e.masses_g).forEach((m,i)=>assert(Math.abs(m-r.masses[i][1])<1e-10));assert(Math.abs(r.sum-300)<1e-10);}
for(const v of [{...base,gly:0},{...base,fill:0},{...base,fines:100},{...base,mg:101},{...base,ind:101},{...base,mode:'PI'},{...base,min:-1},{...base,batch:Infinity}])assert.throws(()=>ctx.window.calculateM3(v));
const pct=ctx.window.calculateM3({...base,fill:23.75}),ug=ctx.window.calculateM3({...base,fill:23.75,mode:'ug',mg:37.5});assert(Math.abs(pct.mgUg-35.625)<1e-10);assert(Math.abs(ug.mgUg-37.5)<1e-10);for(const r of [pct,ug]){assert(Math.abs(r.indUg-110)<1e-10);assert(Math.abs(r.glyUg-50)<1e-10)}
nodes['gly-penalty'].value='1';nodes['stability-penalty'].value='1';vm.runInContext('mcda()',ctx);assert(nodes['mcda-result'].innerHTML.includes('3,59'));
for(const [k,v] of Object.entries({'cost-ngi':100,'cost-dd':10,'cost-batch':500,'cost-other':1000}))nodes[k].value=String(v);vm.runInContext('costs()',ctx);assert.equal(nodes['cost-result'].textContent.replace(/\s/g,''),'13080,00€');
assert(nodes['power-chart'].innerHTML.includes('<polyline'));assert(nodes['astra-heat'].innerHTML.includes('F01'));assert.equal((nodes['experiments'].innerHTML.match(/<details>/g)||[]).length,16);
assert(!/<(?:script|link|img)\b[^>]*(?:src|href)="https?:/.test(html));
const report={status:'PASS_STATIC_AND_NUMERICAL',documents_bytes_verified:data.docs.length,astra_rows:19,fable_rows:15,experiments:16,power_scenarios:72,js_examples_match_python:4,invalid_inputs_rejected:8,mcda_sensitivity:'3.59',cost_formula:'13080 EUR for test inputs',external_runtime_dependencies:0,visual_browser_check:'NOT_COMPLETED_LOCAL_FILE_BLOCKED_BY_BROWSER_POLICY'};
console.log(JSON.stringify(report));
