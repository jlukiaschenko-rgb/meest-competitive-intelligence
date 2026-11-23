(()=>{
"use strict";
const $=id=>document.getElementById(id);
const esc=v=>String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const safe=u=>{try{const a=new URL(u);return ["https:","http:"].includes(a.protocol)?a.href:"#"}catch{return "#"}};
const domains={"Nova Post":"novapost.com","epaka.pl":"epaka.pl","Furgonetka.pl":"furgonetka.pl","GlobKurier":"globkurier.pl","Przesyłarka.pl":"przesylarka.pl","Poczta Polska":"poczta-polska.pl","Apaczka":"apaczka.pl","Sendit":"sendit.pl"};
const names=Object.keys(domains);
const metaUrl=n=>"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=PL&q="+encodeURIComponent(n);
const googleUrl=n=>"https://adstransparency.google.com/?region=PL&domain="+encodeURIComponent(domains[n]||"");
const trendsUrl=n=>"https://trends.google.com/trends/explore?geo=PL&date=today%203-m&q="+encodeURIComponent(n);
const verifiedStatus=s=>s==="potwierdzona_na_stronie";
function render(data){
 const panel=$("campaign-data"); const selector=$("campaign-brand"),count=$("campaign-count");
 const campaigns=Array.isArray(data.campaigns)?data.campaigns:[];
 const chosen=selector.value;
 const filtered=campaigns.filter(c=>!chosen||c.competitor===chosen);
 count.textContent=filtered.length+" opisanych działań";
 panel.innerHTML=filtered.length?filtered.map(c=>`
  <article class="campaign-card">
    <div class="campaign-meta"><span class="campaign-label verified">Potwierdzona na stronie</span><span class="campaign-label">${esc(c.competitor)}</span><span class="campaign-label">${esc(c.type||"Działanie marketingowe")}</span></div>
    <h3>${esc(c.title)}</h3>
    <p>${esc(c.description)}</p>
    <p><strong>Co to znaczy dla Meest Post?</strong> ${esc(c.insight||"Do dalszej analizy.")}</p>
    ${c.valid_until?'<p><strong>Podana data końcowa:</strong> '+esc(c.valid_until)+'</p>':''}
    <div class="campaign-links">
      <a href="${safe(c.source_url)}" target="_blank" rel="noopener noreferrer">Oficjalne źródło ↗</a>
      <a href="${safe(metaUrl(c.competitor))}" target="_blank" rel="noopener noreferrer">Sprawdź reklamy Meta ↗</a>
      <a href="${safe(googleUrl(c.competitor))}" target="_blank" rel="noopener noreferrer">Sprawdź reklamy Google ↗</a>
    </div>
  </article>`).join(""):'<div class="campaign-empty">Dla tej firmy nie potwierdzono publicznej kampanii w tym przeglądzie. Możesz sprawdzić reklamy w Meta i Google przez odnośniki poniżej.</div>';
 const company=chosen||"Nova Post";
 $("campaign-quicklinks").innerHTML='<a href="'+safe(metaUrl(company))+'" target="_blank" rel="noopener noreferrer">Meta Ads: '+esc(company)+' ↗</a> · <a href="'+safe(googleUrl(company))+'" target="_blank" rel="noopener noreferrer">Google Ads: '+esc(company)+' ↗</a> · <a href="'+safe(trendsUrl(company))+'" target="_blank" rel="noopener noreferrer">Google Trends: '+esc(company)+' ↗</a>';
 $("campaign-updated").textContent="Przegląd źródeł: "+esc(data.updated_at||"—")+" · Aktywności reklam płatnych nie potwierdzono";
}
async function boot(){
 const select=$("campaign-brand");
 if(!select)return;
 select.innerHTML='<option value="">Wszystkie firmy</option>'+names.map(n=>'<option value="'+esc(n)+'">'+esc(n)+'</option>').join("");
 try{
  const res=await fetch("./data/campaigns.json?"+Date.now(),{cache:"no-store"});
  if(!res.ok)throw new Error("HTTP "+res.status);
  const data=await res.json();
  select.addEventListener("change",()=>render(data));
  render(data);
 }catch(err){
  $("campaign-data").innerHTML='<div class="campaign-empty">Nie udało się pobrać katalogu kampanii: '+esc(err.message)+'</div>';
  $("campaign-count").textContent="Błąd danych";
 }
}
boot();
})();