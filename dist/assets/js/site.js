(function(){
  var d=document, w=window; d.documentElement.classList.add('js');
  var reduce = w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header */
  var header=d.querySelector('.site-header');
  function onScroll(){ if(header){ header.classList.toggle('is-scrolled', w.scrollY>24); } }
  onScroll(); w.addEventListener('scroll', onScroll, {passive:true});

  /* mobile menu */
  var btn=d.querySelector('.menu-btn'), nav=d.querySelector('.nav');
  if(btn&&nav){ btn.addEventListener('click', function(){ var open=nav.classList.toggle('open'); btn.setAttribute('aria-expanded', open?'true':'false'); }); }

  /* hero ring: scroll-linked rotation on top of the idle spin */
  var heroRing=d.querySelector('.ring-hero .spin-scroll');
  if(heroRing && !reduce){
    var ticking=false;
    function rot(){ heroRing.style.transform='rotate('+(w.scrollY*0.045)+'deg)'; ticking=false; }
    w.addEventListener('scroll', function(){ if(!ticking){ w.requestAnimationFrame(rot); ticking=true; } }, {passive:true});
  }

  /* flywheel steps */
  var fw=d.querySelector('.flywheel');
  if(fw && 'IntersectionObserver' in w){
    var steps=[].slice.call(fw.querySelectorAll('.fw-step'));
    fw.setAttribute('data-step','1');
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){
          steps.forEach(function(s){ s.classList.remove('is-active'); });
          e.target.classList.add('is-active');
          fw.setAttribute('data-step', e.target.getAttribute('data-n'));
        }
      });
    }, {rootMargin:'-45% 0px -45% 0px', threshold:0});
    steps.forEach(function(s){ io.observe(s); });
  }

  /* reveal */
  if('IntersectionObserver' in w){
    var rv=[].slice.call(d.querySelectorAll('.rv'));
    var ro=new IntersectionObserver(function(entries){ entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); ro.unobserve(e.target);} }); }, {rootMargin:'0px 0px -8% 0px'});
    rv.forEach(function(el){ var r=el.getBoundingClientRect(); if(r.top < w.innerHeight){ el.classList.add('in'); } else { ro.observe(el); } });
  } else { [].forEach.call(d.querySelectorAll('.rv'), function(el){ el.classList.add('in'); }); }

  /* form error from redirect */
  var err=d.querySelector('.form-error'), em=/[?&]error=(\d)/.exec(location.search);
  if(err && em){ var span=err.querySelector('[data-err="'+em[1]+'"]')||err.querySelector('[data-err="2"]'); if(span){ span.classList.add('show'); } err.classList.add('show'); err.scrollIntoView({block:'center'}); }
  var ts=d.querySelector('input[name=ts]'); if(ts){ ts.value=String(Math.floor(Date.now()/1000)); }
})();
