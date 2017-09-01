clear;clc;
[num,player,season,time,reb,ast,ste,blo,tov,ppg,win,lose] = textread('resultWhole.txt','%s%s%s%s%s%s%s%s%s%s%s%s','delimiter', ',');
fprintf('reading finished!');
DataStr = [num,player,season,time,reb,ast,ste,blo,tov,ppg,win,lose];
% removing head
Data = [season,time,reb,ast,ste,blo,tov,ppg,win,lose];
Data(1,:) = [];
%DataMissOri = [time,hit_rate,fr_throw,reb,ste,blo,tov,ppg,win,lose];
all = Data;
all_pre = Data;

[ro,co] = size(all_pre);
    
all_pre_double = zeros(ro,co+1);

for ic = 1:co
    for ir = 1:ro
        index(ir,:) = ir;
    end
    for ir=1:ro
        % if missing
        if (strcmp(all_pre(ir,ic),'?'))
            % find previous index
            for previous = ir:-1:1
                if (~strcmp(all_pre(previous,ic),'?'))
                    break;
                end
            end            
            % find next index         
            for next = ir:ro
                if (~strcmp(all_pre(next,ic),'?'))
                    break;
                end               
            end
            % average
            all_pre_double(ir,ic) = 0.5*(str2double(all_pre(previous,ic))+str2double(all_pre(next,ic)));
            
        else
            all_pre_double(ir,ic) = str2double(all_pre(ir,ic));
        end
    end  
end
% adding win_rate 
all_pre_double(:,co+1) =  all_pre_double(:,co-1)./(all_pre_double(:,co-1)+all_pre_double(:,co));
fprintf('Pre-treatment finished!');
% save data
filename = 'final_data_whole.csv';
fid = fopen(filename, 'w');
% writing head
fprintf(fid, '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,', DataStr{1,:});
fprintf(fid, '%s,\n', 'win_rate');
for ir = 1:ro
    % rewriting num
    fprintf(fid, '%d,', ir);
    % rewriting player
    fprintf(fid, '%s,', player{ir+1,1});
    % rewriting new data
    for ic = 1:co           
        fprintf(fid, '%f,', all_pre_double(ir,ic));
    end
    fprintf(fid, '%f,\n', all_pre_double(ir,co+1));
end
fclose(fid);
fprintf('Writing finished!');
