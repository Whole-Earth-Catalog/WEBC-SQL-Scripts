CREATE TABLE tag245 (
	col_id varchar(100),
	col_1 varchar(100),
	col_4 varchar(100),
	col_5 varchar(100),
	col_6 varchar(100),
	col_a varchar(5470),
	col_b varchar(100),
	col_c varchar(100),
	col_d varchar(100),
	col_e varchar(100),
	col_f varchar(100),
	col_g varchar(100),
	col_h varchar(100),
	col_i varchar(100),
	col_k varchar(100),
	col_l varchar(100),
	col_m varchar(100),
	col_n varchar(100),
	col_o varchar(100),
	col_p varchar(100),
	col_q varchar(100),
	col_r varchar(100),
	col_s varchar(100),
	col_t varchar(100),
	col_u varchar(100),
	col_v varchar(100),
	col_w varchar(100),
	col_x varchar(100)
);
LOAD DATA LOCAL INFILE "245.tsv"
INTO TABLE tag245
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';
CREATE TABLE tag100 (
	col_id varchar(100),
	col_1 varchar(100),
	col_4 varchar(100),
	col_6 varchar(100),
	col_a varchar(512),
	col_b varchar(100),
	col_c varchar(100),
	col_d varchar(100),
	col_e varchar(100),
	col_f varchar(100),
	col_g varchar(100),
	col_h varchar(100),
	col_j varchar(100),
	col_k varchar(100),
	col_l varchar(100),
	col_n varchar(100),
	col_p varchar(100),
	col_q varchar(100),
	col_s varchar(100),
	col_t varchar(100),
	col_u varchar(100),
	col_v varchar(100),
	col_x varchar(100)
);
LOAD DATA LOCAL INFILE "100.tsv"
INTO TABLE tag100
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';
CREATE TABLE tag260 (
	col_id varchar(100),
	col_3 varchar(100),
	col_5 varchar(100),
	col_6 varchar(100),
	col_a varchar(100),
	col_b varchar(1112),
	col_c varchar(100),
	col_d varchar(100),
	col_e varchar(100),
	col_f varchar(100),
	col_g varchar(100),
	col_m varchar(100),
	col_n varchar(100),
	col_p varchar(100),
	col_s varchar(100),
	col_v varchar(100),
	col_x varchar(100),
	col_z varchar(100)
);
LOAD DATA LOCAL INFILE "260.tsv"
INTO TABLE tag260
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';
