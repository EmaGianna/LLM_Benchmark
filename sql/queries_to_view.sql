
--Vista Gemma7
CREATE VIEW gemma_7b_data1
AS 
select s.id_promtp 
	  ,s.complejidad 
	  ,s.prompt 
	  ,seg.answers 
from set_1 s  
inner join "set_1_gemma:7b" seg 
on s.id_promtp = seg.id_prompts;

--Vista llama2
CREATE VIEW llama2_data1 
AS 
select s.id_promtp 
	  ,s.complejidad 
	  ,s.prompt 
	  ,sll2.answers 
from set_1 s  
inner join "set_1_llama2" sll2 
on s.id_promtp = sll2.id_prompts;

--Vista llama3
CREATE VIEW llama3_data1 
AS 
select s.id_promtp 
	  ,s.complejidad 
	  ,s.prompt 
	  ,sll3.answers 
from set_1 s  
inner join "set_1_llama3" sll3
on s.id_promtp = sll3.id_prompts;


--Vista extra_muy_alto_gemma_7
CREATE VIEW extra_muy_alto_gemma_7
AS 
select sema7.id_promtp 
	  ,sema7.complejidad 
	  ,sema7.prompt 
	  ,semag7.answers 
from 'set_Extra_Muy_Alto' sema7  
inner join "set_Extra_Muy_Alto_gemma:7b" semag7
on sema7.id_promtp = semag7.id_prompts;


--Vista extra_muy_alto_llama2
CREATE VIEW extra_muy_alto_llama2
AS 
select sema7.id_promtp 
	  ,sema7.complejidad 
	  ,sema7.prompt 
	  ,semall2.answers 
from 'set_Extra_Muy_Alto' sema7  
inner join "set_Extra_Muy_Alto_llama2" semall2
on sema7.id_promtp = semall2.id_prompts;


--Vista extra_muy_alto_llama2
CREATE VIEW extra_muy_alto_llama3
AS 
select sema7.id_promtp 
	  ,sema7.complejidad 
	  ,sema7.prompt 
	  ,semall3.answers 
from 'set_Extra_Muy_Alto' sema7  
inner join "set_Extra_Muy_Alto_llama3" semall3
on sema7.id_promtp = semall3.id_prompts;


